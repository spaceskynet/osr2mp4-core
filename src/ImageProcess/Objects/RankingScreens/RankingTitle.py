from PIL import Image

from ... import imageproc
from .ARankingScreen import ARankingScreen
from ...PrepareFrames.Components.Text import prepare_text
from ....global_var import Settings


class RankingTitle(ARankingScreen):
	def __init__(self, frames, replayinfo, beatmap):
		dummy = [Image.new("RGBA", (1, 1))]
		super().__init__(dummy)
		self.replayinfo = replayinfo
		self.artist = beatmap.meta["Artist"]
		self.beatmapname = beatmap.meta["Title"]
		self.mapper = beatmap.meta["Creator"]
		self.diff = beatmap.meta["Version"]
		self.player = replayinfo.player_name
		self.date = str(replayinfo.timestamp)
		self.date = self.date.replace("-", "/")

		self.rankingtitle = frames[0]

		titleimg = prepare_text(["{} - {} [{}]".format(self.artist, self.beatmapname, self.diff)], 40, (255, 255, 255, 255))
		creatorimg = prepare_text(["Beatmap by {}".format(self.mapper)], 30, (255, 255, 255, 255))
		playerimg = prepare_text(["Played by {} on {}".format(self.player, self.date)], 30, (255, 255, 255, 255))

		self.textimgs = {**titleimg, **creatorimg, **playerimg}

	def drawname(self, background, x_offset, y_offset, text, alpha, size):
		imageproc.add(self.textimgs[text], background, x_offset, y_offset, alpha=alpha, topleft=True)

	def add_to_frame(self, background, np_img):
		super().add_to_frame(background)
		if self.fade == self.FADEIN:
			self.drawname(background, 0, 0 * Settings.scale, "{} - {} [{}]".format(self.artist, self.beatmapname, self.diff), self.alpha, 0.75)
			self.drawname(background, 0, 35 * Settings.scale, "Beatmap by {}".format(self.mapper), self.alpha, 0.5)
			self.drawname(background, 0, 60 * Settings.scale, "Played by {} on {}".format(self.player, self.date), self.alpha, 0.5)

			imageproc.add(self.rankingtitle, background, Settings.width - 32 * Settings.scale - self.rankingtitle.size[0], 10 * Settings.scale, self.alpha, topleft=True)
