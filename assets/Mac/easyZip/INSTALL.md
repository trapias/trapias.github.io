# Installing easyZip

easyZip is currently distributed as an **ad-hoc signed** application
(not yet notarized by Apple). macOS Gatekeeper will block the first
launch with a message like *"easyZip can't be opened because Apple
cannot check it for malicious software."*

## One-time setup

1. Drag **easyZip.app** from this DMG into your **Applications** folder.
2. Open Terminal (⌘+Space → "Terminal") and paste this command, then
   press Enter:

   ```
   xattr -cr /Applications/easyZip.app
   ```

   This removes the quarantine flag macOS attached to the download.
   It does **not** grant any extra privilege; it just tells Gatekeeper
   to trust the bundle the same way you would trust an app you
   compiled yourself.
3. Eject the DMG (drag to Trash or `diskutil eject`).
4. Open easyZip from Launchpad, Spotlight, or `/Applications`.

You only need to run the `xattr` command **once**, per installation.
Future Sparkle auto-updates do not re-add the quarantine flag.

## Why is this necessary?

Apple's Developer Program (which would let me notarize the bundle so
this step is unnecessary) costs **$99/year**. Until easyZip earns
back its hosting and Developer fees, the build is signed with an
ad-hoc identity and the `xattr` workaround is the official Apple
recommendation for users who trust the source.

If you'd rather not run the command, easyZip is open source — clone
the repo from <https://github.com/trapias/easyZip>, run
`Scripts/install.sh`, and the same install lands on your Mac without
the quarantine flag in the first place.

## Auto-updates

easyZip uses [Sparkle](https://sparkle-project.org) for automatic
updates. New releases are signed with an Ed25519 key and verified on
your machine before installation. You can disable update checks under
**easyZip → Settings → Updates**.

## Uninstall

```
rm -rf /Applications/easyZip.app
defaults delete it.trapias.easyzip   # clears recents + preferences
security delete-generic-password -s it.trapias.easyzip.archive-password   # clears saved Keychain passwords (run once per password)
```
