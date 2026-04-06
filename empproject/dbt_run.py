from dbt.cli.main import dbtRunner, dbtRunnerResult

# Initialize the dbt runner
dbt = dbtRunner()

# Define the command arguments
# Specify project and profiles directories if they are not in the current working directory
# args = ["run", "--project-dir", "/path/to/my/dbt_project", "--profiles-dir", "/path/to/my/profiles"]
args = ["run", "--select", "cust_subscriber2.sql", "--profile", "empproject", "--target", "STG"]

# Invoke the command
res: dbtRunnerResult = dbt.invoke(args)

# Check the results
if res.success:
    print("dbt run completed successfully!")
else:
    print(f"dbt run failed: {res.error}")
