# cr2jpg

Small script I use to turn Canon CR2 raw files into JPGs. It uses rawpy (LibRaw) to decode the raw with the camera's white balance, then saves a JPG with Pillow.

## Usage

You need [uv](https://docs.astral.sh/uv/). It installs rawpy and Pillow on the first run.

```
./cr2jpg.py ~/Pictures/Japan
```

The JPGs go next to the CR2 files unless you pass `-o`:

```
./cr2jpg.py ~/Pictures/Japan -o ~/Pictures/Japan-jpg
```

Options:

```
-o, --out DIR      output folder (default: the input folder)
-q, --quality N    JPG quality, default 95
-f, --force        overwrite JPGs that already exist
```

Without `-f` it skips any photo that already has a JPG, so running it twice on the same folder is safe.

It only looks at the top level of the folder, not subfolders. I've only tried it on macOS with files from a Canon body. Other raw formats LibRaw supports would probably work if you change the `.cr2` check, but I haven't tested that.
