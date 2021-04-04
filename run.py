from somo import create_app, db
app = create_app()
# app.app_context().push()
# db.drop_all()
# db.create_all()
import click
from read import write, add_all


@app.cli.command()
def add_a():
    """Add Grades and subjects"""
    click.echo('----Adding all----')
    add_all()
    click.echo('----done adding all----')


@app.cli.command()
def add_data():
    """Add Students"""
    click.echo("----adding students----")

    write()
    click.echo("----Done!----")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
