import os
from pathlib import Path


TEXT = (
    "A mountain does not watch the clouds go by. It lets them come, "
    "lets them rest on its shoulders a while, lets them leave. "
    "It has stood through a million such evenings. "
    "It will be standing through yours."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
