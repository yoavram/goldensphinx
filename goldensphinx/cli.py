# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import subprocess
import shlex

import static
import click
import sphinx

import goldensphinx


app = static.Cling('.')


@click.group(chain=True)
@click.version_option(version=goldensphinx.__version__, prog_name=goldensphinx.__name__)
def cli():
	if os.environ.get('SPHINX', 'true').lower() == 'false':
		return


@cli.command()
@click.option('--static_dir', default="docs/_build/html", envvar="STATIC_DIR", type=click.Path(), help="Static directory to serve")
@click.option('--host', default='0.0.0.0', envvar="HOST", help="Hostname to serve on")
@click.option('--port', default=8000, envvar="PORT", help="Port to serve on")
@click.option('--num_threads', default=16, envvar="NUM_SERVER_THREADS", help="Number of threads")
def serve(static_dir, host, port, num_threads):
	if not os.path.exists(static_dir):
		raise click.ClickException('Invalid value for "--static_dir": Path "{}" does not exist.'.format(static_dir))
	prev_dir = os.getcwd()
	os.chdir(static_dir)
	cmd = 'gunicorn goldensphinx:app -b {host}:{port} -w {num_threads} -k gevent -t 2 --name goldensphinx'
	cmd = cmd.format(port=port, host=host, static_dir=static_dir, num_threads=num_threads)
	args = shlex.split(cmd)
	res = subprocess.run(args).returncode
	os.chdir(prev_dir)
	return res


@cli.command()
@click.option('--source_dir', default='docs', envvar="DOCS_DIR", type=click.Path(exists=True), help="Directory containing documentation source")
@click.option('--dest_dir', default='docs/_build/html', envvar="STATIC_DIR", type=click.Path(writable=True), help="Directory to build documentation to")
def build(source_dir, dest_dir):
	click.echo(
		"Building Sphinx from {source_dir} to {dest_dir}...".format(
			source_dir=source_dir, dest_dir=dest_dir)
		)
	sphinx.build_main([
		'setup.py', 
		'-b', 'html', 
		source_dir, 
		dest_dir
	])


if __name__ == '__main__':
	print('result:', cli(auto_envvar_prefix=goldensphinx.__name__.upper()))
