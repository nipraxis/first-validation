""" First validation
"""

from pathlib import Path

from hashlib import sha1

data_pth = Path() / 'data'
example_pth =  data_pth / '24719.f3_beh_CHYM.csv'

if not example_pth.is_file():
    raise RuntimeError('Have you run the "get_data.py" script?')

contents = example_pth.read_bytes()
hash_value = sha1(contents).hexdigest()

print(f'Hash value for {example_pth} is {hash_value}')

hashes_pth = data_pth / 'data_hashes.txt'

print(f'Contents of {hashes_pth}')
hashes_text = hashes_pth.read_text()
print(hashes_text)


def hash_for_fname(fname):
    """ Return SHA1 hash string for file in `fname`

    `fname` can be a string or a Path.
    """
    # Convert a string filename to a Path object.
    fpath = Path(fname)
    # Your code here.
    return 'not-really-the-hash'


# Fill in the function above to make the test below pass.
# The test passes when there is no error.
calc_hash = hash_for_fname(example_pth)
exp_hash = '7fa09f0f0dc11836094b8d360dc63943704796a1'
assert calc_hash == exp_hash, f'{calc_hash} does not match {exp_hash}'


def check_hashes(hash_fname, data_dir):
    """ Check hashes and filenames in given in file `hash_fname`.

    `hash_fname` is a filename or Path of a file containing lines like::

        7fa09f0f0dc11836094b8d360dc63943704796a1  24719.f3_beh_CHYM.csv

    where the first string is the SHA1 hash for the file, and the second is the
    filename.  The filename is relative to the `data_dir` directory.

    Parameters
    ----------
    hash_fname : str or Path
        String giving filename of text file containing hash value, filename
        pairs, or Path object pointing to file, e.g. "data/data_hashes.txt".
    data_dir : str or Path
        String giving directory containing files named in `hash_fname` above,
        e.g. "data"

    Returns
    -------
    all_ok : {True or False}
        Return True if all the hashes recorded in `hash_fname` match the
        calculated hashes for the corresponding filenames, False if any of the
        hashes do not match.
    """
    # Convert hash and directory to Path objects for convenience.
    hash_pth = Path(hash_fname)
    data_dir = Path(data_dir)
    # Read in text for hash filename
    # Split into lines.
    # For each line:
        # Split each line into expected_hash and filename
        # Calculate actual hash for given filename.
        # Check actual hash against expected hash
        # Return False if any of the hashes do not match.
    return True


# Correct hash list file returns True
assert check_hashes(hashes_pth, data_pth), \
        'Check hash list does not return True'
# Incorrect hash list files return False
test_dir = Path('tests')
assert not check_hashes(test_dir / 'first_bad.txt', data_pth), \
        'first_bad has bad first hash, should give False'
assert not check_hashes(test_dir / 'second_bad.txt', data_pth), \
        'second_bad has bad second hash, should give False'
assert not check_hashes(test_dir / 'last_bad.txt', data_pth), \
        'last_bad has bad last hash, should give False'

print('Finished.')
