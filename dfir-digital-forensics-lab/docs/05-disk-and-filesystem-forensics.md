# 05 — Disk and Filesystem Forensics

## 1. Storage concepts

A storage device may contain a partition table, partitions, filesystems, allocated files, unallocated space, and filesystem metadata. A logical file copy is not the same as a physical or forensic image.

## 2. Acquisition types

- **Logical acquisition:** collects selected files or directories visible through the operating system.
- **Physical acquisition:** aims to acquire addressable storage sectors, subject to device and tool constraints.
- **Live acquisition:** collects from a running system; useful for some volatile or encrypted states but changes system state.
- **Dead-box acquisition:** examines a powered-off source or an acquired image.

Select the method based on authorization, incident needs, encryption state, operational risk, and policy. Document exclusions and errors.

## 3. Filesystem concepts

Learn the metadata structures and recovery behavior of:
- NTFS: Master File Table (MFT), file records, timestamps, alternate data streams, and USN Change Journal.
- FAT/exFAT: directory entries and allocation structures.
- ext4: inodes, directory entries, journals, and timestamps.

The exact artefacts available depend on filesystem state, OS version, and acquisition quality.

## 4. Deleted data and carving

Deletion often removes or changes filesystem references before the underlying data is overwritten. Recovery may be partial or impossible. File carving searches for known file signatures in raw data but may lose filenames, paths, and context. Recovered fragments must be validated and interpreted cautiously.

## 5. Common tools

- Autopsy / The Sleuth Kit: disk-image examination and filesystem analysis.
- FTK Imager: acquisition and image review in supported workflows.
- Guymager: imaging utility commonly used in Linux forensic environments.
- ewf-tools: utilities for supported Expert Witness Format images.

Check official documentation, version compatibility, licensing, and organizational approval before use.

## Practical exercise

Use a purpose-built training image or an image you created from a disposable VM that you own. Do not image a personal or third-party device without authorization.

1. Record image source, acquisition method, tool version, and hash.
2. Open a verified working copy in an approved forensic tool.
3. Identify partitions and filesystem types.
4. Examine a small set of training files and metadata.
5. Export selected artefacts to a separate analysis directory.
6. Hash exported files and document how they relate to the source.
7. Write a short findings note with limitations.

Never publish a disk image or recovered personal files in this repository.
