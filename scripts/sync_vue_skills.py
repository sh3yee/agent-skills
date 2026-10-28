"""Mirror the selected vuejs-ai skills without changing locally owned skills."""

import argparse
from pathlib import Path
import shutil


SKILLS = (
    "create-adaptable-composable",
    "vue-best-practices",
    "vue-debug-guides",
    "vue-jsx-best-practices",
    "vue-options-api-best-practices",
    "vue-pinia-best-practices",
    "vue-router-best-practices",
    "vue-testing-best-practices",
)


def sync_skills(upstream: Path, repository: Path) -> None:
    upstream = upstream.resolve()
    repository = repository.resolve()
    vue = repository / "vue"
    license_source = upstream / "LICENSE"
    license_target = vue / "LICENSE.vuejs-ai"

    # Validate the complete input and all deletion targets before changing files.
    if vue.is_symlink() or vue.resolve().parent != repository:
        raise ValueError(f"Vue directory must stay inside the repository: {vue}")
    if not license_source.is_file() or license_source.is_symlink():
        raise ValueError(f"Missing upstream license or unsupported symlink: {license_source}")
    if license_target.is_symlink() or (license_target.exists() and not license_target.is_file()):
        raise ValueError(f"License target must be a regular file: {license_target}")

    for name in SKILLS:
        source = upstream / "skills" / name
        target = vue / name
        if not (source / "SKILL.md").is_file():
            raise ValueError(f"Missing upstream skill: {source / 'SKILL.md'}")
        if source.is_symlink() or any(path.is_symlink() for path in source.rglob("*")):
            raise ValueError(f"Upstream skill contains unsupported symlinks: {source}")
        if target.is_symlink() or target.resolve().parent != vue:
            raise ValueError(f"Sync target must stay inside the Vue directory: {target}")
        if target.exists() and not target.is_dir():
            raise ValueError(f"Sync target must be a directory: {target}")

    vue.mkdir(parents=True, exist_ok=True)
    for name in SKILLS:
        target = vue / name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(upstream / "skills" / name, target)
        print(f"Synced {name}")
    shutil.copy2(license_source, license_target)
    print("Synced upstream license")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("upstream", type=Path, help="Path to a vuejs-ai/skills checkout")
    args = parser.parse_args()
    sync_skills(args.upstream, Path(__file__).resolve().parents[1])
