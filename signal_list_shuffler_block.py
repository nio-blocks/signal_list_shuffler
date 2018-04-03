import random
from nio.block.base import Block
from nio.properties import VersionProperty, Property


class SignalListShuffler(Block):

    version = VersionProperty('0.1.0')
    seed = Property(
        title='Random Seed', default=None, allow_none=True, visible=False)

    def configure(self, context):
        super().configure(context)
        if self.seed():
            random.seed(int(self.seed()))

    def process_signals(self, signals):
        random.shuffle(signals)
        self.notify_signals(signals)
