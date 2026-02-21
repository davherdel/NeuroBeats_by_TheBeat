import subprocess
import os
import sys

# ================= CONFIG =================

BITRATE = "256k"   # 192k, 256k, 320k
OUT_EXT = ".m4a"

# =========================================


def get_file_size_mb(path: str) -> float:
    return os.path.getsize(path) / (1024 * 1024)


def compress_wav_to_m4a(input_wav: str, output_m4a: str, bitrate: str = BITRATE):

    if not os.path.isfile(input_wav):
        raise FileNotFoundError(f"Input file not found: {input_wav}")

    cmd = [
        "ffmpeg",
        "-y",                       # overwrite output
        "-i", input_wav,            # input
        "-vn",                      # no video
        "-map_metadata", "0",       # keep metadata
        "-c:a", "aac",              # codec
        "-b:a", bitrate,            # bitrate
        "-movflags", "+faststart",  # better for web players
        output_m4a
    ]

    print("Running ffmpeg:")
    print(" ".join(cmd))

    subprocess.run(cmd, check=True)


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python compress_audio_for_canva.py input.wav [output.m4a]")
        sys.exit(1)

    input_wav = sys.argv[1]

    if len(sys.argv) >= 3:
        output_m4a = sys.argv[2]
    else:
        base, _ = os.path.splitext(input_wav)
        output_m4a = base + "_canva.m4a"

    print("\n--- File sizes ---")
    print(f"Input : {get_file_size_mb(input_wav):.2f} MB")

    compress_wav_to_m4a(input_wav, output_m4a)

    print(f"Output: {get_file_size_mb(output_m4a):.2f} MB")
    print("\nDone.")


if __name__ == "__main__":
    main()
