# Releasing WNAI

This dataset is curated using `pydplace`. See the [README](https://github.com/D-PLACE/pydplace?tab=readme-ov-file#release-workflow) for release instructions.


## Notes

The map must be created **without** the `--pacific-centered` option, i.e. running
```shell
$ cldfbench cldfviz.map cldf  --format png --width 20 --output map.png --with-ocean --no-legend
```
