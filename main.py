import os
import sys
import tempfile
from pathlib import Path


TEXT = (
    "A mountain does not watch the clouds go by. It lets them come, "
    "lets them rest on its shoulders a while, lets them leave. "
    "It has stood through a million such evenings. "
    "It will be standing through yours."
)


def main() -> int:
    count = len(TEXT)
    if not 1 <= count <= 280:
        print(
            f"Error: entry text must contain 1..280 Unicode code points; got {count}.",
            file=sys.stderr,
        )
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        temporary_path = None
        try:
            with tempfile.NamedTemporaryFile(
                dir=output_dir, prefix=".entry-", suffix=".tmp", delete=False
            ) as temporary_file:
                temporary_path = Path(temporary_file.name)
                temporary_file.write(TEXT.encode("utf-8"))
            os.replace(temporary_path, output_dir / "entry.txt")
        finally:
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
    except OSError as exc:
        print(f"Error: could not write entry.txt in {output_dir}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
