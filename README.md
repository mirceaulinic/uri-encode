# uri-encode

Docker image to encode arbitrary strings. For lazy people.

Usage:

```bash
$ docker run --rm mirceaulinic/uri-encode Hellö Wörld@Python
Hell%C3%B6 W%C3%B6rld%40Python
```

Or define an alias, e.g.,

```bash
function uri-encode(){
    docker run --rm mirceaulinic/uri-encode $@
}
```

And use:

```bash
$ uri-encode Hellö Wörld@Python
```
