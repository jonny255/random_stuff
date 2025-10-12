<<<<<<< HEAD
Perfect — let’s set this up in a way that’s forensically sound and won’t risk trashing your client’s Windows HDD. You already know the source (/dev/sda) and the recovery drive (/mnt/rescue on /dev/sdc1). Here’s the industry-standard step-by-step:
Step 1. Prep the environment
Make sure rescue disk is mounted:
mkdir -p /mnt/rescue
mount /dev/sdc1 /mnt/rescue

Step 2. Forensic image the client HDD
Do a first non-retry pass:
ddrescue -f -n /dev/sda /mnt/rescue/client_hdd.img /mnt/rescue/client_hdd.log

If no errors, you can still run a retry pass (safe but optional):
ddrescue -d -r3 /dev/sda /mnt/rescue/client_hdd.img /mnt/rescue/client_hdd.log

Step 3. Work from the image, not the disk
Detach the client drive. Everything from here is against client_hdd.img.
Associate with loop device:
losetup --find --show -P /mnt/rescue/client_hdd.img

That’ll return something like /dev/loop2. You’ll then see partitions at /dev/loop2p1, /dev/loop2p2, /dev/loop2p3, etc.
Step 4. Mount NTFS partition read-only
Client said Windows is on sda3 → now it’s loop2p3.
 Mount it read-only to avoid corruption:
mkdir -p /mnt/client
mount -t ntfs-3g -o ro /dev/loop2p3 /mnt/client

Step 5. Copy recovered data
Now you can rsync from the read-only mount into your recovery area:
rsync -avh --progress /mnt/client/ /mnt/rescue/client_data/

Step 6. Optional: force mount if client insists on "bootable recovery"
If Windows must boot (rare in forensic jobs), you can force remove hibernation file only against the image:
mount -t ntfs-3g -o remove_hiberfile /dev/loop2p3 /mnt/client

⚠️ Never do this against /dev/sda. Always against the .img.
✅ End result:
Original disk untouched.
Bit-for-bit clone in /mnt/rescue/client_hdd.img.
Client data safely extracted to /mnt/rescue/client_data.
Do you want me to also show you how to validate the .img hash (MD5/SHA256) so you can prove to the client it’s an exact copy? That’s a common forensic step.
Alright — here’s how you validate and document the integrity of that forensic image:
Step 1. Hash the original drive (before unplugging it)
Run against the raw block device:
sha256sum /dev/sda > /mnt/rescue/client_hdd.sha256

This gives you a baseline fingerprint of the entire disk.
Step 2. Hash the image
Run against the .img file you created:
sha256sum /mnt/rescue/client_hdd.img >> /mnt/rescue/client_hdd.sha256

Step 3. Compare
Open the .sha256 file:
cat /mnt/rescue/client_hdd.sha256

You should see two identical SHA256 values — one for /dev/sda and one for client_hdd.img.
 If they match → your image is a verified 1:1 copy.
Step 4. (Optional) Generate MD5 for compatibility
Some tools/clients want MD5 instead of SHA256:
md5sum /dev/sda > /mnt/rescue/client_hdd.md5
md5sum /mnt/rescue/client_hdd.img >> /mnt/rescue/client_hdd.md5

At that point you can hand the client:
client_hdd.img (their full disk clone)
client_data/ (their extracted files)
=======
Perfect — let’s set this up in a way that’s forensically sound and won’t risk trashing your client’s Windows HDD. You already know the source (/dev/sda) and the recovery drive (/mnt/rescue on /dev/sdc1). Here’s the industry-standard step-by-step:
Step 1. Prep the environment
Make sure rescue disk is mounted:
mkdir -p /mnt/rescue
mount /dev/sdc1 /mnt/rescue

Step 2. Forensic image the client HDD
Do a first non-retry pass:
ddrescue -f -n /dev/sda /mnt/rescue/client_hdd.img /mnt/rescue/client_hdd.log

If no errors, you can still run a retry pass (safe but optional):
ddrescue -d -r3 /dev/sda /mnt/rescue/client_hdd.img /mnt/rescue/client_hdd.log

Step 3. Work from the image, not the disk
Detach the client drive. Everything from here is against client_hdd.img.
Associate with loop device:
losetup --find --show -P /mnt/rescue/client_hdd.img

That’ll return something like /dev/loop2. You’ll then see partitions at /dev/loop2p1, /dev/loop2p2, /dev/loop2p3, etc.
Step 4. Mount NTFS partition read-only
Client said Windows is on sda3 → now it’s loop2p3.
 Mount it read-only to avoid corruption:
mkdir -p /mnt/client
mount -t ntfs-3g -o ro /dev/loop2p3 /mnt/client

Step 5. Copy recovered data
Now you can rsync from the read-only mount into your recovery area:
rsync -avh --progress /mnt/client/ /mnt/rescue/client_data/

Step 6. Optional: force mount if client insists on "bootable recovery"
If Windows must boot (rare in forensic jobs), you can force remove hibernation file only against the image:
mount -t ntfs-3g -o remove_hiberfile /dev/loop2p3 /mnt/client

⚠️ Never do this against /dev/sda. Always against the .img.
✅ End result:
Original disk untouched.
Bit-for-bit clone in /mnt/rescue/client_hdd.img.
Client data safely extracted to /mnt/rescue/client_data.
Do you want me to also show you how to validate the .img hash (MD5/SHA256) so you can prove to the client it’s an exact copy? That’s a common forensic step.
Alright — here’s how you validate and document the integrity of that forensic image:
Step 1. Hash the original drive (before unplugging it)
Run against the raw block device:
sha256sum /dev/sda > /mnt/rescue/client_hdd.sha256

This gives you a baseline fingerprint of the entire disk.
Step 2. Hash the image
Run against the .img file you created:
sha256sum /mnt/rescue/client_hdd.img >> /mnt/rescue/client_hdd.sha256

Step 3. Compare
Open the .sha256 file:
cat /mnt/rescue/client_hdd.sha256

You should see two identical SHA256 values — one for /dev/sda and one for client_hdd.img.
 If they match → your image is a verified 1:1 copy.
Step 4. (Optional) Generate MD5 for compatibility
Some tools/clients want MD5 instead of SHA256:
md5sum /dev/sda > /mnt/rescue/client_hdd.md5
md5sum /mnt/rescue/client_hdd.img >> /mnt/rescue/client_hdd.md5

At that point you can hand the client:
client_hdd.img (their full disk clone)
client_data/ (their extracted files)
>>>>>>> 8b61bde744b4df973a47574f8b29e0afad188e4b
client_hdd.sha256 (your forensic proof)