#!/usr/bin/python3

########################################################################################
#
#
#
########################################################################################
####[ Imports ]#########################################################################


from time import asctime
from os import path
from shutil import disk_usage


####[ Functions ]#######################################################################


def get_meminfo(convert_memory_size_to, decimal_conversion):
    """"""
    # TODO: Figure out how to do swap like I did memory
    # The information to be retrieved
    items = {
        "MemTotal": [],
        "MemFree": [],  # Temporary
        "MemUsed": [],
        "Buffers": [],  # Temporary
        "Cached": [],  # Temporary
        "SReclaimable": [],  # Temporary
    }
    items_keys = list(items.keys())

    # If the end user wants the data to be displayed using 1024 byte conversion,
    # this if statement converts the......................
    if not decimal_conversion:
        mult = 0.9765625
    else:
        mult = 1.0

    # Retrieving information and adding it to the 'items' dict
    for line in open("/proc/meminfo").readlines():
        split_line = line.split()
        if split_line[0].rstrip(":") in items_keys:
            items[split_line[0].rstrip(":")].append(float(split_line[1]) * mult)
            items[split_line[0].rstrip(":")].append("K")

    # Memory Used = (MemTotal - MemFree - Buffers - (Cached + KReclaimable))
    # See more in `man 1 free`
    items["MemUsed"].append(
        int(
            items["MemTotal"][0]
            - items["MemFree"][0]
            - items["Buffers"][0]
            - (items["Cached"][0] + items["SReclaimable"][0])
        )
    )
    items["MemUsed"].append("K")

    # Remove temporary keys
    items.pop("MemFree")
    items.pop("Buffers")
    items.pop("Cached")
    items.pop("SReclaimable")

    # Convert unit size of data (1000KB --> 1MB)
    items["MemTotal"] = convert_size(
        items["MemTotal"], convert_memory_size_to, decimal_conversion
    )
    items["MemUsed"] = convert_size(
        items["MemUsed"], items["MemTotal"][1][0], decimal_conversion
    )

    return items


# TODO: Input the conversion stuff so that it's outcome is similar to the way I have
#  it in get_meminfo
def get_mount(convert_disk_size_to, decimal_conversion, disk_verbose):
    """"""
    items = {"/": {"total": [0, "B"], "used": [0, "B"]}}

    # Retrieving information and adding it to the 'items' dict
    if disk_verbose:
        for line in open("/proc/mounts").readlines():
            split_line = line.split()
            if path.exists(split_line[0]):
                items[split_line[1]] = {
                    "total": [list(disk_usage(split_line[1]))[0], "B"],
                    "used": [list(disk_usage(split_line[1]))[1], "B"],
                }
    else:
        for line in open("/proc/mounts").readlines():
            split_line = line.split()
            if path.exists(split_line[0]):
                items["/"] = {
                    "total": [
                        list(disk_usage(split_line[1]))[0] + items["/"]["total"][0],
                        "B",
                    ],
                    "used": [
                        list(disk_usage(split_line[1]))[1] + items["/"]["used"][0],
                        "B",
                    ],
                }

    # Convert unit size of data (1000KB --> 1MB)
    for mount_location in items:
        for form in items[mount_location]:
            items[mount_location][form] = list(
                convert_size(
                    items[mount_location][form],
                    convert_disk_size_to,
                    decimal_conversion,
                )
            )

    return items


# TODO: Work on this/make it look and function better
#  Try to get it to work with only one char instead of the whole string
def convert_size(byte_amount, convert_to, decimal_conversion):
    """"""
    units = ["", "K", "M", "G", "T", "P", "E", "Z", "Y"]

    if decimal_conversion:
        units_prefix = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
        byte_conv_size = 1000
    else:
        units_prefix = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
        byte_conv_size = 1024

    if convert_to is not None:
        if convert_to != "B" and convert_to not in units:
            raise ValueError("convert_size: Invalid convert_to '{}'".format(convert_to))

    start = 0 if byte_amount[1] == "B" else units.index(byte_amount[1])
    stop = int(len(units) - 1)

    if convert_to is None:
        for unit in range(start, stop):
            if byte_amount[0] < byte_conv_size or units[unit] == "Y":
                return [round(byte_amount[0], 2), units_prefix[unit]]
            byte_amount[0] /= byte_conv_size
    else:
        for unit in range(start, stop):
            if units[unit] == convert_to or units[unit] == convert_to:
                return [round(byte_amount[0], 2), units_prefix[unit]]
            byte_amount[0] /= byte_conv_size

    raise Exception("convert_size: Couldn't return converted list")


def main(
    memory_percent,
    disk_percent,
    disk_verbose,
    decimal_conversion,
    convert_memory_size_to,
    convert_disk_size_to,
):
    """"""
    mem_info = get_meminfo(convert_memory_size_to, decimal_conversion)
    """Contains all the memory based information."""
    mount_info = get_mount(convert_disk_size_to, decimal_conversion, disk_verbose)
    """Contains all the information regarding the size of all mounted _____."""
    mount_keys = list(mount_info.keys())
    mem_used = "{}{}".format(mem_info["MemUsed"][0], mem_info["MemTotal"][1])
    """Combines the amount of used memory with the unit type (i.e. GB)."""
    mem_total = "{}{}".format(mem_info["MemTotal"][0], mem_info["MemTotal"][1])
    """Combines the amount of total memory with the unit type (i.e. GB)."""
    mem_percent = "{}%".format(
        round(
            (mem_info["MemUsed"][0] / mem_info["MemTotal"][0]) * 100,
            2,
        )
    )
    """Calculates the percentage of memory used."""

    print("  System information as of {}\n".format(asctime()))
    # Prints out CPU usage and number of users logged into the server
    print("  CPU usage:    {}Users logged in: {}".format(temp_var.ljust(31), temp_var))
    # ....
    if memory_percent:
        print(
            "  Memory Usage: {} / {} {}".format(
                mem_used, mem_total, ("(" + str(mem_percent) + ")")
            )
        )
    # ....
    else:
        print("  Memory Usage: {} / {}".format(mem_used, mem_total))
    # ....
    if disk_verbose:
        print("  Disk Usage:")
        for i in mount_keys:
            print(
                "    Usage of {}: {}{} / {}{}{}".format(
                    mount_keys[mount_keys.index(i)].ljust(34),
                    str(mount_info[i]["used"][0]).ljust(7),
                    mount_info[i]["used"][1],
                    str(mount_info[i]["total"][0]).ljust(7),
                    mount_info[i]["total"][1],
                    (
                        " ("
                        + str(
                            round(
                                (mount_info[i]["used"][0] / mount_info[i]["total"][0])
                                * 100
                            )
                        )
                        + "%)"
                    )
                    if disk_percent
                    else "",
                )
            )
    # ....
    else:
        print(
            "  Disk Usage:   {}{} / {}{}{}".format(
                str(mount_info["/"]["used"][0]),
                mount_info["/"]["used"][1],
                str(mount_info["/"]["total"][0]),
                mount_info["/"]["total"][1],
                (
                    " ("
                    + str(
                        round(
                            (
                                mount_info["/"]["used"][0]
                                / mount_info["/"]["total"][0]
                                * 100
                            ),
                            2,
                        )
                    )
                    + "%)"
                    if disk_percent
                    else ""
                ),
            )
        )


####[ Main ]############################################################################


if __name__ == "__main__":
    temp_var = "xxxxxx"
    MEMORY_PERCENT = True
    DISK_PERCENT = True
    DISK_VERBOSE = False
    DECIMAL_CONVERSION = True
    CONVERT_MEMORY_SIZE_TO = None
    CONVERT_DISK_SIZE_TO = None

    main(
        MEMORY_PERCENT,
        DISK_PERCENT,
        DISK_VERBOSE,
        DECIMAL_CONVERSION,
        CONVERT_MEMORY_SIZE_TO,
        CONVERT_DISK_SIZE_TO,
    )
