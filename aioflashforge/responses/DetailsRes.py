from dataclasses import dataclass
from typing import Any


@dataclass
class DetailsRes:
    autoShutdown: str
    autoShutdownTime: int
    cameraStreamUrl: str
    chamberFanSpeed: int
    chamberTargetTemp: int
    chamberTemp: int
    coolingFanSpeed: int
    cumulativeFilament: float
    cumulativePrintTime: int
    currentPrintSpeed: int
    doorStatus: str
    errorCode: str
    estimatedLeftLen: int
    estimatedLeftWeight: float
    estimatedRightLen: int
    estimatedRightWeight: float
    estimatedTime: float
    externalFanStatus: str
    fillAmount: int
    firmwareVersion: str
    flashRegisterCode: str
    internalFanStatus: str
    ipAddr: str
    leftFilamentType: str
    leftTargetTemp: int
    leftTemp: int
    lightStatus: str
    location: str
    macAddr: str
    measure: str
    name: str
    nozzleCnt: int
    nozzleModel: str
    nozzleStyle: int
    pid: int
    platTargetTemp: float
    platTemp: float
    polarRegisterCode: str
    printDuration: int
    printFileName: str
    printFileThumbUrl: str
    printLayer: int
    printProgress: float
    printSpeedAdjust: float
    remainingDiskSpace: float
    rightFilamentType: str
    rightTargetTemp: float
    rightTemp: float
    status: str
    targetPrintLayer: int
    tvoc: int
    zAxisCompensation: float

    @staticmethod
    def from_dict(obj: Any) -> 'DetailsRes':
        _autoShutdown = str(obj.get("autoShutdown"))
        _autoShutdownTime = int(obj.get("autoShutdownTime"))
        _cameraStreamUrl = str(obj.get("cameraStreamUrl"))
        _chamberFanSpeed = int(obj.get("chamberFanSpeed"))
        _chamberTargetTemp = int(obj.get("chamberTargetTemp"))
        _chamberTemp = int(obj.get("chamberTemp"))
        _coolingFanSpeed = int(obj.get("coolingFanSpeed"))
        _cumulativeFilament = float(obj.get("cumulativeFilament"))
        _cumulativePrintTime = int(obj.get("cumulativePrintTime"))
        _currentPrintSpeed = int(obj.get("currentPrintSpeed"))
        _doorStatus = str(obj.get("doorStatus"))
        _errorCode = str(obj.get("errorCode"))
        _estimatedLeftLen = int(obj.get("estimatedLeftLen"))
        _estimatedLeftWeight = float(obj.get("estimatedLeftWeight"))
        _estimatedRightLen = int(obj.get("estimatedRightLen"))
        _estimatedRightWeight = float(obj.get("estimatedRightWeight"))
        _estimatedTime = float(obj.get("estimatedTime"))
        _externalFanStatus = str(obj.get("externalFanStatus"))
        _fillAmount = int(obj.get("fillAmount"))
        _firmwareVersion = str(obj.get("firmwareVersion"))
        _flashRegisterCode = str(obj.get("flashRegisterCode"))
        _internalFanStatus = str(obj.get("internalFanStatus"))
        _ipAddr = str(obj.get("ipAddr"))
        _leftFilamentType = str(obj.get("leftFilamentType"))
        _leftTargetTemp = int(obj.get("leftTargetTemp"))
        _leftTemp = int(obj.get("leftTemp"))
        _lightStatus = str(obj.get("lightStatus"))
        _location = str(obj.get("location"))
        _macAddr = str(obj.get("macAddr"))
        _measure = str(obj.get("measure"))
        _name = str(obj.get("name"))
        _nozzleCnt = int(obj.get("nozzleCnt"))
        _nozzleModel = str(obj.get("nozzleModel"))
        _nozzleStyle = int(obj.get("nozzleStyle"))
        _pid = int(obj.get("pid"))
        _platTargetTemp = float(obj.get("platTargetTemp"))
        _platTemp = float(obj.get("platTemp"))
        _polarRegisterCode = str(obj.get("polarRegisterCode"))
        _printDuration = int(obj.get("printDuration"))
        _printFileName = str(obj.get("printFileName"))
        _printFileThumbUrl = str(obj.get("printFileThumbUrl"))
        _printLayer = int(obj.get("printLayer"))
        _printProgress = float(obj.get("printProgress"))
        _printSpeedAdjust = float(obj.get("printSpeedAdjust"))
        _remainingDiskSpace = float(obj.get("remainingDiskSpace"))
        _rightFilamentType = str(obj.get("rightFilamentType"))
        _rightTargetTemp = float(obj.get("rightTargetTemp"))
        _rightTemp = float(obj.get("rightTemp"))
        _status = str(obj.get("status"))
        _targetPrintLayer = int(obj.get("targetPrintLayer"))
        _tvoc = int(obj.get("tvoc"))
        _zAxisCompensation = float(obj.get("zAxisCompensation"))
        return DetailsRes(
            _autoShutdown, _autoShutdownTime, _cameraStreamUrl,
            _chamberFanSpeed, _chamberTargetTemp, _chamberTemp,
            _coolingFanSpeed, _cumulativeFilament, _cumulativePrintTime,
            _currentPrintSpeed, _doorStatus, _errorCode, _estimatedLeftLen,
            _estimatedLeftWeight, _estimatedRightLen, _estimatedRightWeight,
            _estimatedTime, _externalFanStatus, _fillAmount, _firmwareVersion,
            _flashRegisterCode, _internalFanStatus, _ipAddr, _leftFilamentType,
            _leftTargetTemp, _leftTemp, _lightStatus, _location, _macAddr,
            _measure, _name, _nozzleCnt, _nozzleModel, _nozzleStyle, _pid,
            _platTargetTemp, _platTemp, _polarRegisterCode, _printDuration,
            _printFileName, _printFileThumbUrl, _printLayer, _printProgress,
            _printSpeedAdjust, _remainingDiskSpace, _rightFilamentType,
            _rightTargetTemp, _rightTemp, _status, _targetPrintLayer,
            _tvoc, _zAxisCompensation
        )


@dataclass
class RootDetailsRes:
    code: int
    detail: DetailsRes
    message: str

    @staticmethod
    def from_dict(obj: Any) -> 'RootDetailsRes':
        _code = int(obj.get("code"))
        _detail = DetailsRes.from_dict(obj.get("detail"))
        _message = str(obj.get("message"))
        return RootDetailsRes(_code, _detail, _message)
