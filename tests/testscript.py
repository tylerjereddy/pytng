import pytng

file_iterator = pytng.TNGFileIterator("./reference_files/argon_npt_compressed.tng", mode="r", debug=True)
file_iterator.read_frame(0)
file_iterator.read_frame(10000)
# file_iterator.read_all_frames()
