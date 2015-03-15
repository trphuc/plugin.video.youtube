# ENDPOINTS
## Videos
### Play a video via ID
```
plugin://plugin.video.youtube/play/?video_id=[VID]
```
## Playlists
### Show videos of a playlist
```
plugin://plugin.video.youtube/playlist/[PID]/
```
### Default executing a playlist:
```
plugin://plugin.video.youtube/play/?playlist_id=[PID]
```
### Play a playlist in a specified order:
```
plugin://plugin.video.youtube/play/?playlist_id=[PID]&order=[default|reverse|shuffle]
```
### Play a playlist with a starting video:
```
plugin://plugin.video.youtube/play/?playlist_id=[PID]&video_id=[VID]
```
## Channels
### Navigate to a channel via ID:
```
plugin://plugin.video.youtube/channel/[CID]/
```
### Navigate to a channel via username:
```
plugin://plugin.video.youtube/user/[NAME]/
```
