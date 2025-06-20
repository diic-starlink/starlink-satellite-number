from build_stats import analyze

CONSTELLATIONS = {
    "Starlink": "./starlink_satcat.json",
    "OneWeb": "./oneweb_satcat.json",
    "O3B": "./o3b_satcat.json",
    "Project Kuiper": "./kuiper_satcat.json",
}


def main():
    for constellation_name, data_file in CONSTELLATIONS.items():
        analyze(constellation_name, data_file)


if __name__ == "__main__":
    main()
