# Golden Sphinx

Build and serve Sphinx docs.

Example usage:

```sh
$ goldensphinx build serve
```

You can also just build:

```sh
$ goldensphinx build
```

or just serve:

```sh
$ goldensphinx serve
```

To see the options you can control, run a command with `--help`:

```sh
$ goldensphinx build --help
Usage: goldensphinx build [OPTIONS]

Options:
  --source_dir PATH  Directory containing documentation source
  --dest_dir PATH    Directory to build documentation to
  --help             Show this message and exit.

$ goldensphinx serve --help
Usage: goldensphinx serve [OPTIONS]

Options:
  --static_dir PATH      Static directory to serve
  --host TEXT            Hostname to serve on
  --port INTEGER         Port to serve on
  --num_threads INTEGER  Number of threads
  --help                 Show this message and exit.
```

All options can be also be set using environment variables:

- `source_dir` and `static_dir` by `STATIC_DIR`
- `dest_dir` by `DOCS_DIR`
- `port` by `PORT`
- `host` by `HOST`
- `num_threads` by `NUM_SERVER_THREADS`

For example:

```sh
$ export PORT=8080
$ goldensphinx serve --host 127.0.0.1
[2016-09-06 10:02:14 +0300] [55096] [INFO] Starting gunicorn 19.6.0
[2016-09-06 10:02:14 +0300] [55096] [INFO] Listening at: http://127.0.0.1:8080 (87302)
```

## Install

Stable:

```sh
pip install goldensphinx
```

Latest:

```sh
pip install git+https://github.com/yoavram/goldensphinx.git
```

## Authors

- Yoav Ram (@yoavram)

## Acknowledgements

- The project is inspired by, and the `serve` command is modified from [kennethreitz/goldenarch](https://github.com/kennethreitz/goldenarch).
- Many thanks to the authors of Python, Gunicorn, Sphinx, Click, Static and everything else we build our apps with.
