# Retro OS Themes for Home Assistant

[![Open in Home Assistant Marketplace](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=Tropie1988&repository=home-assistant-retro-themes&category=theme)

Remember the look of Windows 95, Mac OS 8 or Amiga Workbench? This collection brings a bit of that nostalgia to Home Assistant. It includes **16 themes** inspired by classic operating systems, from monochrome Macintosh to the colorful desktops of the late '90s.

Pick any theme from your Home Assistant profile. No custom cards or frontend add-ons are needed.

## See them in action

These screenshots show the themes on my Home Assistant dashboard. The cards, entities and dashboard layout are just examples; the themes change the appearance of your own setup.

### Mac OS 8 Platinum

![Mac OS 8 Platinum on a Home Assistant dashboard](assets/screenshots/macos-8-platinum-clean.png)

<details>
<summary>More screenshots: Windows, BeOS, Solaris, Macintosh and Amiga</summary>

### Windows Classic

![Windows Classic on a Home Assistant dashboard](assets/screenshots/windows-classic-clean.png)

### BeOS R5 Tracker

![BeOS R5 Tracker on a Home Assistant dashboard](assets/screenshots/beos-r5-tracker-clean.png)

### Solaris CDE Motif

![Solaris CDE Motif on a Home Assistant dashboard](assets/screenshots/solaris-cde-motif-clean.png)

### Classic Macintosh

![Classic Macintosh on a Home Assistant dashboard](assets/screenshots/classic-macintosh-clean.png)

### Amiga Workbench 2.x

![Amiga Workbench 2.x on a Home Assistant dashboard](assets/screenshots/amiga-workbench-2x-clean.png)

</details>

## The 16 themes

| Family | Themes |
| --- | --- |
| Windows | Windows 3.1 Program Manager · Windows 95 Classic · Windows 98 Classic · Windows NT 4.0 Workstation · Windows 2000 Professional · Windows XP Luna Blue |
| Classic Mac | Macintosh System 6 Monochrome · Macintosh System 7 Classic · Mac OS 8 Platinum · Mac OS 9 Platinum |
| Modern Mac | Mac OS X 10.0 - Cheetah Aqua |
| Other classics | OS2 Warp 4 Merlin · Amiga Workbench 2.x · Solaris CDE Motif · BeOS R5 Tracker · Apple Lisa Office System |

## Install

### From the Home Assistant Marketplace

1. Open **Settings → Marketplace** and search for **Retro OS Themes**.
2. Install the collection.
3. Open your **user profile → Theme** and choose one of the 16 themes.

You can also use the Marketplace button at the top of this page. All 16 choices come in one installable theme bundle.

### Manually

1. Download [`themes/retro_os_collection.yaml`](themes/retro_os_collection.yaml) and copy it to `/config/themes/retro_os_collection.yaml`.
2. Add the following to your Home Assistant `configuration.yaml` if you haven't already configured themes. If you have a `frontend:` block, add the `themes:` line inside it instead of creating a second block:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

3. Run the `frontend.reload_themes` action (or restart Home Assistant), then pick a theme from your profile.

## A few details

The themes change colors, borders, corners, shadows and the look of cards, the sidebar and the toolbar. Fonts are used where they're available on your device. Home Assistant cards and frontend versions can render some details differently; these are themes for Home Assistant, not recreations of the original operating systems or their desktop features.

Mac OS 8 Platinum is the version I use myself. Its active icons have a little more contrast while keeping the classic Platinum palette.

## For contributors

The individual YAML files live in [`source/`](source/). [`tools/build.py`](tools/build.py) combines them into the single [Marketplace bundle](themes/retro_os_collection.yaml). If you change a theme, edit its source file and rebuild the bundle:

```bash
python tools/build.py
python -m pip install PyYAML
python tools/validate.py
python tools/build.py --check
```

GitHub Actions runs these checks and HACS validation for each change. If you find a rough edge, [open an issue](https://github.com/Tropie1988/home-assistant-retro-themes/issues).

## License

The themes are original configurations inspired by historical operating systems. This repository isn't affiliated with their creators and doesn't include proprietary artwork, font files or logos. Released under the [MIT License](LICENSE).
