from click.testing import CliRunner

from pipelines.run import run_build_database


def test_build_database_last_year():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(run_build_database, ["--refresh-type", "last"])

        # TODO: Add SQL check to verify that the last year was processed

        assert result.exit_code == 0
