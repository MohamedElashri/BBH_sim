import nox


@nox.session(python=["3.10", "3.11", "3.12"])
def tests(session):
    session.install("pytest")
    session.install(".")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("flake8", "black")
    session.run("flake8", "BBH_SIM")
    session.run("black", "--check", ".")


@nox.session
def format(session):
    session.install("black")
    session.run("black", ".")
