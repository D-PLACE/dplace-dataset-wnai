# Releasing the ea


```shell
cldfbench makecldf cldfbench_wnai.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench cldfviz.map cldf --pacific-centered --format png --width 20 --output map.png --with-ocean
```

```shell
cldfbench readme cldfbench_wnai.py
cldfbench zenodo --communities dplace cldfbench_wnai.py
dplace check cldfbench_wnai.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_wnai.py vX.Y
```