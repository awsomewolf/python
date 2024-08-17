class Television:
    """
    A class that operates a TV Remote
    MIN_VOLUME: is the minimum volume
    MAX_VOLUME = is the maximum volume
    MIN_CHANNEL = is the minimum channel
    MAX_CHANNEL = is the maximum channel
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to set default values of TV Settings
        status: Is the TV on or off?
        muted: Is the TV muted?
        volume: The TV's volume
        channel: The TV's channel
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn the TV on and off
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to mute or unmute the TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method to increase the channel
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the channel
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume
        """
        if self.__status:
            if not self.__muted:
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1
            else:
                self.__muted = False
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume
        """
        if self.__status:
            if not self.__muted:
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1
            else:
                self.__muted = False
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to print the variables
        :return: TV settings
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
