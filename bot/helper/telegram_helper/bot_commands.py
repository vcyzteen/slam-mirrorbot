class _BotCommands:
    def __init__(self):
        self.StartCommand = 'iopi'
        self.MirrorCommand = 'iopilink'
        self.UnzipMirrorCommand = 'iopiunzip'
        self.TarMirrorCommand = 'iopitar'
        self.CancelMirror = 'iopicancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'iopilist'
        self.StatusCommand = 'iopistatus'
        self.AuthorizeCommand = 'authorize'
        self.UnAuthorizeCommand = 'unauthorize'
        self.PingCommand = 'iopiping'
        self.RestartCommand = 'iopirestart'
        self.StatsCommand = 'iopistats'
        self.HelpCommand = 'iopihelp'
        self.LogCommand = 'iopilog'
        self.SpeedCommand = 'iopispeedtest'
        self.CloneCommand = "iopiclone"
        self.WatchCommand = 'iopiwatch'
        self.TarWatchCommand = 'iopitarwatch'
        self.DeleteCommand = 'iopidel'
        self.UsageCommand = 'iopiusage'

BotCommands = _BotCommands()
