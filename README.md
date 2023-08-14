# First validation

Make sure you have followed the [installation
instructions](https://textbook.nipraxis.org/installation).  You will need
Git, Python and the various Python libraries installed.

```
cd $HOME/Documents
```

```{warning}
If you get `The system cannot find the path specified`, and you are on Windows,
make sure you are running a **Powershell** shell, not the much older Windows `cmd` shell.

If you get this message, and you are trying things on out a JupyterHub or other
Linux system, check that the `Documents` directory exists in your home
directory, and, if not, create it with `mkdir $HOME/Documents`.
```

Make a new directory to store your work, if you have not already done this in
the [installation instructions](https://textbook.nipraxis.org/installation).

```
mkdir nipraxis-work
```

Change your shell to that directory:

```
cd nipraxis-work
```

Next go to this page : <https://github.com/nipraxis/first-validation>

Click on the "Fork" button on the mid-top-right.

Accept the defaults and click on "Create fork"

You will find yourself at the page for your new Fork.  In my case that is <https://github.com/matthew-brett/first-validation> but the address will have your username in it, rather than `matthew-brett`.

Copy the URL.

Clone the repository from the command line, by typing `git clone` at the
terminal and then copy-pasting the URL.  For example, for me, that would be
`git clone https://github.com/matthew-brett/first-validation` **but you need to
make sure you clone your own fork, with your own URL**.

```
# Your git clone command here:
git clone https://github.com/your-github-username/first-validation
```

Next:

```
cd first-validation
# Show the files
ls
```

We are going to be working on some fixes, to be proposed to the *upstream
repository* at <https://github.com/nipraxis/first-validation>.  The upstream repository is the repository from which you created your fork above.

Whenever we work on a new set of changes we make a new *branch*.

We do that like this:

```
# Create the branch (bookmark).
git branch fix-validation
```

```
# Show the branches verbosely (-v).  Notice the asterisk on "main".
git branch -v
```

```
# Checkout the branch ready for work.
git checkout fix-validation
```

```
# Show the branches verbosely (-v).  Notice the asterisk on "fix-validation".
git branch -v
```

Now you are ready to do the work.  First get the images you need.

```
python3 get_data.py
```

You should see something like this:

```
Saving files to "data" directory
Fetched mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii to /Users/mb312/Library/Caches/nipraxis/0.4/mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii
Copied /Users/mb312/Library/Caches/nipraxis/0.4/mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii to data/mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii
Fetched ds114_sub009_highres_brain_222.nii to /Users/mb312/Library/Caches/nipraxis/0.4/ds114_sub009_highres_brain_222.nii
Copied /Users/mb312/Library/Caches/nipraxis/0.4/ds114_sub009_highres_brain_222.nii to data/ds114_sub009_highres_brain_222.nii
Fetched 24719.f3_beh_CHYM.csv to /Users/mb312/Library/Caches/nipraxis/0.4/24719.f3_beh_CHYM.csv
Copied /Users/mb312/Library/Caches/nipraxis/0.4/24719.f3_beh_CHYM.csv to data/24719.f3_beh_CHYM.csv
Contents of "data" subdirectory:
   data/mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii
   data/24719.f3_beh_CHYM.csv
   data/ds114_sub009_highres_brain_222.nii
```

You will see a different cache directory in the printout above.  My cache
directory was `/Users/mb312/Library/Caches/nipraxis/0.4/` but your directory
will be specific to you, and the current version of the `nipraxis` module.

If there are any errors, let us know.

Check the files are in the `data` sub-directory with:

```
ls data
```

You will see an extra file in that directory, called `data_hashes.txt`.

Next run the as-yet-unfixed data validation script:

```
python3 first_validation.py
```

Notice the output.  Notice too that you get an `AssertionError`.  This is the error you are aiming to fix.

Open the script in a text editor.  At a pinch you can open in Textedit (Mac) or
Wordpad (Windows).   On Unix you can use the Nano editor (use `nano` at the
command line).  At a pinch you can even use the Jupyter Notebook itself,
opening the `first_validation.py` file from the notebook interface.

Look at the script.  Edit the script to fix the assertion error.  Run `python first_validation.py` again.  You should see another, new `AssertionError`.  If you have time, try fixing that error.

When you are ready, or you think you are going to run out of time, save your changes, and check that Git can see you have made changes with:

```
git status
```

You should `first_validation.py` in red, with changes that have not been staged ready for commit.

Now, put the changes into the Git staging area:

```
git add first_validation.py
```

Show the changes are now in the staging area with:

```
# Notice the filename should now be in green.
git status
```

Make a commit.  For now (and only for now) use the `-m` flag to add a commit
message:

```
git commit -m "Fixes to the validation script"
```

Finally, push the changes up to your *fork*:

```
git push origin fix-validation --set-upstream
```

You will see a message at the console telling you the link to go to, to make a
pull request.  In my case that link was
"https://github.com/matthew-brett/first-validation/pull/new/fix-validation",
but your link will be different, because it will contain your own Github user
name.

Go to that URL in your browser.

Type something about your changes into the "Description".

Click on "Create pull request".

You should see a new page with your pull request.
