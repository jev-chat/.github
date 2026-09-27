"""把 profile/assets/src/ 下的 HTML 渲染成 README 用的 PNG（浅色 / 深色各一张）。

用法（在仓库根目录）：
    python profile/assets/src/render.py            # 全部重出
    python profile/assets/src/render.py card-ios   # 只出名字里含 card-ios 的

依赖：本机 Chrome（无头模式）+ Pillow + imagequant（pip install pillow imagequant；
没装 imagequant 会退回 Pillow 自带量化，渐变处会有色块）。出图按 2 倍像素，再量化成 256 色调色板 PNG，
单张目标 ≤ 150KB。拉丁字体 Figtree 放在 fonts/ 里（官网同款），中文用系统字体（Windows 上是微软雅黑），出图不联网。
"""
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
SRC = pathlib.Path(__file__).resolve().parent
OUT = SRC.parent
SCALE = 2
LIMIT = 150_000  # 字节，按十进制 150KB 算，留足余量

# 名字、页面（可带查询参数）、CSS 宽、CSS 高。四张平台卡顺序固定：Android → Windows → iOS → macOS。
JOBS = [
    ("banner", "banner.html", 880, 470),
    ("card-android", "card.html?p=android", 176, 252),
    ("card-windows", "card.html?p=windows", 176, 252),
    ("card-ios", "card.html?p=ios", 176, 252),
    ("card-macos", "card.html?p=macos", 176, 252),
    ("core-flow", "flow.html", 880, 380),
]


def shoot(page: str, theme: str, w: int, h: int, raw: pathlib.Path, profile: pathlib.Path) -> None:
    path, _, query = page.partition("?")
    url = (SRC / path).as_uri() + "?" + "&".join(x for x in (query, f"theme={theme}") if x)
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--no-first-run",
            f"--user-data-dir={profile}",
            f"--force-device-scale-factor={SCALE}",
            f"--window-size={w},{h}",
            "--default-background-color=00000000",
            "--virtual-time-budget=3000",
            f"--screenshot={raw}",
            url,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=90,
    )


def quantize(img: Image.Image, colors: int) -> Image.Image:
    # 优先用 libimagequant（pngquant 同一套算法，渐变和阴影不出色块）：pip install imagequant
    try:
        import imagequant

        return imagequant.quantize_pil_image(img, dithering_level=1.0, max_colors=colors)
    except ImportError:
        return img.quantize(colors=colors, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG)


def squeeze(raw: pathlib.Path, out: pathlib.Path) -> int:
    img = Image.open(raw).convert("RGBA")
    for colors in (256, 224, 192, 160, 128):
        quantize(img, colors).save(out, optimize=True)
        size = out.stat().st_size
        if size <= LIMIT:
            return size
    return size


def main() -> None:
    only = sys.argv[1:]
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="jev-profile-render-"))
    try:
        for name, page, w, h in JOBS:
            if only and not any(o in name for o in only):
                continue
            for theme in ("light", "dark"):
                raw = tmp / f"{name}-{theme}.raw.png"
                shoot(page, theme, w, h, raw, tmp / "chrome-profile")
                out = OUT / f"{name}-{theme}.png"
                size = squeeze(raw, out)
                flag = "" if size <= LIMIT else "  <-- 超过 150KB"
                print(f"{out.name:28s} {w * SCALE}x{h * SCALE}  {size / 1024:6.1f} KB{flag}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
