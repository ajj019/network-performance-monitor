import speedtest
import csv
import os
from datetime import datetime


def run_speed_test():
    """
    Runs a speed test and returns timestamp, ping, download speed, and upload speed.
    """
    print("Initializing Speed Test...\n")

    st = speedtest.Speedtest()

    # Find best server based on latency
    st.get_best_server()

    print("Running download test...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps

    print("Running upload test...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    ping = st.results.ping  # Latency in ms

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return timestamp, ping, download_speed, upload_speed


def log_results(timestamp, ping, download, upload):
    """
    Logs the results to a CSV file.
    Creates file with headers if it doesn't exist.
    """
    file_exists = os.path.isfile("network_log.csv")

    with open("network_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "Ping (ms)", "Download (Mbps)", "Upload (Mbps)"])

        writer.writerow([timestamp, round(ping, 2), round(download, 2), round(upload, 2)])


def main():
    timestamp, ping, download, upload = run_speed_test()

    print("\n--- Network Performance Results ---")
    print(f"Time: {timestamp}")
    print(f"Ping (Latency): {ping:.2f} ms")
    print(f"Download Speed: {download:.2f} Mbps")
    print(f"Upload Speed: {upload:.2f} Mbps")

    log_results(timestamp, ping, download, upload)

    print("\nResults logged to network_log.csv")


if __name__ == "__main__":
    main()
