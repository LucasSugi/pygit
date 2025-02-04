from os import popen
from pandas import DataFrame
from re import search
from optparse import OptionParser

# Instantiate object
parser = OptionParser()

# Add arguments
parser.add_option("--git-path", dest = "git_path", type = "str")

# Get all arguments from command line
args, _ = parser.parse_args()

# Parse to dict
args = vars(args)

# Validate args
if args.get("git_path") is None:
    raise KeyError("`git_path` its mandatory")

# Git command to generate the log of commits that delete some file
git_path = args["git_path"]
git_cmd = f"git -C {git_path} log --diff-filter=D --summary"

# Run command of git
raw_data = popen(git_cmd).read()

# Data cleaning
raw_data = [d.strip() for d in raw_data.strip().split("\n") if d != ""]

# Get each the start of each commit on raw_data
commit_index = [i for i in range(len(raw_data)) if search("^commit [a-z0-9]+$", raw_data[i]) is not None]

# List to store data
curated_data = []
for i in range(len(commit_index)-1):

    # Get the limits of commit
    start = commit_index[i]
    end = commit_index[i+1]

    # Get the MR info
    mr_info = raw_data[start:end]

    # Store data
    try:
        curated_data.append({
            "commit": mr_info[0],
            "author": mr_info[1],
            "date": mr_info[2],
            "title": mr_info[3],
            "scripts": mr_info[4:],
        })
    except:
        print(mr_info)

# Create DataFrame from curated_data
curated_data_df = DataFrame(curated_data).explode("scripts")

# Filter just delete mode
filter_delete_mode = curated_data_df.loc[:, "scripts"].map(lambda x: x.startswith("delete mode"))
curated_data_df = curated_data_df.loc[filter_delete_mode, :]

# Cleaning fields
curated_data_df.loc[:, "scripts"] = curated_data_df.loc[:, "scripts"].map(lambda x: x.replace("delete mode ", "").split(" ")[1])
curated_data_df.loc[:, "commit"] = curated_data_df.loc[:, "commit"].map(lambda x: x.replace("commit ", ""))
curated_data_df.loc[:, "author"] = curated_data_df.loc[:, "author"].map(lambda x: x.replace("Author: ", ""))
curated_data_df.loc[:, "date"] = curated_data_df.loc[:, "date"].map(lambda x: x.replace("Date: ", ""))

# Split author into author and email
curated_data_df.loc[:, "email"] = curated_data_df.loc[:, "author"].map(lambda x: search("<.*>", x).group().replace("<","").replace(">", ""))
curated_data_df.loc[:, "author"] = curated_data_df.loc[:, "author"].map(lambda x: x[:x.index("<")-1])

# Fix columns position
select_columns = [
    "commit",
    "scripts",
    "title",
    "author",
    "email",
    "date",
]
curated_data_df = curated_data_df.loc[:, select_columns]

# Save data
(
    curated_data_df
    .to_csv(
        f"{git_path}git_deletion.csv",
        index=False,
        header=True,
        sep=",",
    )
)
