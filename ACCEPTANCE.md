# Validation boundary

- The three integration/arcreel-gpt*.json files target ArcReel's native declarative IMAGE endpoint format. Origin is https://toapis.com (without /v1); the templates include /v1.
- Validate and render them with integration/check-arcreel-contract.py against the pinned upstream source. The upstream validator, six render checks and three credential-placement rejection checks passed.
- Import each definition through ArcReel's supported custom-endpoint workflow and configure the corresponding model/credential. UI import, storage and in-app generation remain untested.
- Video case files are original independent I2V outputs. Native local-first-frame upload is still a gap: do not claim the image endpoint JSON automatically enables native video.
- Vendor-promotion contributions are not accepted as PRs. The upstream contributing guide directs cooperation to support@arc-reel.com; no promotional Issue/PR/Discussion was posted.

No full upstream UI acceptance, native video/reference editing acceptance or audio acceptance is claimed. Check cases.json for API output and billing evidence.
