from ensurepkg import EnsurePkg

for guard in EnsurePkg(dict(dotenv="python-dotenv")):
    with guard:
        import dotenv

with EnsurePkg(dict(git="GitPython"), cache_dir="/tmp/ensurepkg"):
    import git

print(dotenv.__name__)
print(git.__name__, git.__version__)
