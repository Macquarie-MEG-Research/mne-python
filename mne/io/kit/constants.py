"""KIT constants."""

# Authors: Teon Brooks <teon.brooks@gmail.com>
#          Christian Brodbeck <christianbrodbeck@nyu.edu>
#
# License: BSD (3-clause)

from ..constants import FIFF
from ...utils import BunchConst


KIT = BunchConst()

# byte values
KIT.SHORT = 2
KIT.INT = 4
KIT.DOUBLE = 8

# channel parameters
KIT.CALIB_FACTOR = 1.0  # mne_manual p.272
KIT.RANGE = 1.  # mne_manual p.272
KIT.UNIT_MUL = 0  # default is 0 mne_manual p.273
KIT.GAINS = [1, 2, 5, 10, 20, 50, 100, 200]

KIT.HPFS = {
    1: (0, 1, 3, 3),
    2: (0, 1, 3, 0.3),
    3: (0, 0.03, 0.1, 0.3, 1, 3, 10, 30),
    4: (0, 1, 3, 10, 30, 100, 200, 500),
}
KIT.LPFS = {
    1: (10, 20, 50, 100, 200, 500, 1000, 2000),
    3: (10, 20, 50, 100, 200, 500, 1000, 10000),
    4: (10, 30, 100, 300, 1000, 2000, 5000, 10000),
}
KIT.BEFS = {
    1: (0, 50, 60, 60),
    3: (0, 60, 50, 50),
}

# Map FLL-Type to filter options (high, low, band)
KIT.FLL_SETTINGS = {
    0: (1, 1, 1),  # Hanger Type #1
    10: (1, 1, 1),  # Hanger Type #2
    20: (1, 1, 1),  # Hanger Type #2
    50: (2, 1, 1),  # Hanger Type #3
    60: (2, 1, 1),  # Hanger Type #3
    100: (3, 3, 3),  # Low Band Kapper Type
    200: (4, 4, 3),  # High Band Kapper Type
}

# channel types
KIT.CHANNEL_MAGNETOMETER = 1
KIT.CHANNEL_MAGNETOMETER_REFERENCE = 0x101
KIT.CHANNEL_AXIAL_GRADIOMETER = 2
KIT.CHANNEL_AXIAL_GRADIOMETER_REFERENCE = 0x102
KIT.CHANNEL_PLANAR_GRADIOMETER = 3
KIT.CHANNEL_PLANAR_GRADIOMETER_REFERENCE = 0x103
KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER = 4
KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER_REFERENCE = 0x104
KIT.CHANNEL_TRIGGER = -1
KIT.CHANNEL_EEG = -2
KIT.CHANNEL_ECG = -3
KIT.CHANNEL_ETC = -4
KIT.CHANNEL_NULL = 0
KIT.CHANNELS_MEG = (
    KIT.CHANNEL_MAGNETOMETER,
    KIT.CHANNEL_MAGNETOMETER_REFERENCE,
    KIT.CHANNEL_AXIAL_GRADIOMETER,
    KIT.CHANNEL_AXIAL_GRADIOMETER_REFERENCE,
    KIT.CHANNEL_PLANAR_GRADIOMETER,
    KIT.CHANNEL_PLANAR_GRADIOMETER_REFERENCE,
    KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER,
    KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER_REFERENCE,
)
KIT.CHANNELS_REFERENCE = (
    KIT.CHANNEL_MAGNETOMETER_REFERENCE,
    KIT.CHANNEL_AXIAL_GRADIOMETER_REFERENCE,
    KIT.CHANNEL_PLANAR_GRADIOMETER_REFERENCE,
    KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER_REFERENCE,
)
KIT.CHANNELS_MISC = (
    KIT.CHANNEL_TRIGGER,
    KIT.CHANNEL_EEG,
    KIT.CHANNEL_ECG,
    KIT.CHANNEL_ETC,
)
KIT.CH_TO_FIFF_COIL = {
    # KIT.CHANNEL_MAGNETOMETER: FIFF.???,
    KIT.CHANNEL_MAGNETOMETER_REFERENCE: FIFF.FIFFV_COIL_KIT_REF_MAG,
    KIT.CHANNEL_AXIAL_GRADIOMETER: FIFF.FIFFV_COIL_KIT_GRAD,
    # KIT.CHANNEL_AXIAL_GRADIOMETER_REFERENCE: FIFF.???,
    # KIT.CHANNEL_PLANAR_GRADIOMETER: FIFF.???,
    # KIT.CHANNEL_PLANAR_GRADIOMETER_REFERENCE: FIFF.???,
    # KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER: FIFF.???,
    # KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER_REFERENCE: FIFF.???,
    KIT.CHANNEL_TRIGGER: FIFF.FIFFV_COIL_NONE,
    KIT.CHANNEL_EEG: FIFF.FIFFV_COIL_EEG,
    KIT.CHANNEL_ECG: FIFF.FIFFV_COIL_NONE,
    KIT.CHANNEL_ETC: FIFF.FIFFV_COIL_NONE,
    KIT.CHANNEL_NULL: FIFF.FIFFV_COIL_NONE,
}
KIT.CH_TO_FIFF_KIND = {
    KIT.CHANNEL_MAGNETOMETER: FIFF.FIFFV_MEG_CH,
    KIT.CHANNEL_MAGNETOMETER_REFERENCE: FIFF.FIFFV_REF_MEG_CH,
    KIT.CHANNEL_AXIAL_GRADIOMETER: FIFF.FIFFV_MEG_CH,
    KIT.CHANNEL_AXIAL_GRADIOMETER_REFERENCE: FIFF.FIFFV_REF_MEG_CH,
    KIT.CHANNEL_PLANAR_GRADIOMETER: FIFF.FIFFV_MEG_CH,
    KIT.CHANNEL_PLANAR_GRADIOMETER_REFERENCE: FIFF.FIFFV_REF_MEG_CH,
    KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER: FIFF.FIFFV_MEG_CH,
    KIT.CHANNEL_2ND_ORDER_AXIAL_GRADIOMETER_REFERENCE: FIFF.FIFFV_REF_MEG_CH,
    KIT.CHANNEL_TRIGGER: FIFF.FIFFV_MISC_CH,
    KIT.CHANNEL_EEG: FIFF.FIFFV_EEG_CH,
    KIT.CHANNEL_ECG: FIFF.FIFFV_ECG_CH,
    KIT.CHANNEL_ETC: FIFF.FIFFV_MISC_CH,
    KIT.CHANNEL_NULL: FIFF.FIFFV_MISC_CH,
}
KIT.CH_LABEL = {
    KIT.CHANNEL_TRIGGER: 'TRIGGER',
    KIT.CHANNEL_EEG: 'EEG',
    KIT.CHANNEL_ECG: 'ECG',
    KIT.CHANNEL_ETC: 'MISC',
    KIT.CHANNEL_NULL: 'MISC',
}

# Acquisition modes
KIT.CONTINUOUS = 1
KIT.EVOKED = 2
KIT.EPOCHS = 3

# coreg constants
KIT.DIG_POINTS = 10000

# Known KIT systems
# -----------------
# KIT recording system is encoded in the SQD file as integer:
KIT.SYSTEM_MQ_ADULT = 345  # Macquarie Dept of Cognitive Science, 2006 -
KIT.SYSTEM_MQ_CHILD = 403  # Macquarie Dept of Cognitive Science, 2006 -
KIT.SYSTEM_AS = 260  # Academia Sinica at Taiwan
KIT.SYSTEM_AS_2008 = 261  # Academia Sinica, 2008 or 2009 -
KIT.SYSTEM_NYU_2008 = 32  # NYU-NY, July 7, 2008 -
KIT.SYSTEM_NYU_2009 = 33  # NYU-NY, January 24, 2009 -
KIT.SYSTEM_NYU_2010 = 34  # NYU-NY, January 22, 2010 -
KIT.SYSTEM_NYUAD_2011 = 440  # NYU-AD initial launch May 20, 2011 -
KIT.SYSTEM_NYUAD_2012 = 441  # NYU-AD more channels July 11, 2012 -
KIT.SYSTEM_NYUAD_2014 = 442  # NYU-AD move to NYUAD campus Nov 20, 2014 -
KIT.SYSTEM_UMD_2004 = 51  # UMD Marie Mount Hall, October 1, 2004 -
KIT.SYSTEM_UMD_2014_07 = 52  # UMD update to 16 bit ADC, July 4, 2014 -
KIT.SYSTEM_UMD_2014_12 = 53  # UMD December 4, 2014 -
# Sensor layouts, used for plotting and connectivity
KIT_LAYOUT = {
    KIT.SYSTEM_AS: None,
    KIT.SYSTEM_AS_2008: 'KIT-AS-2008',
    KIT.SYSTEM_MQ_ADULT: 'KIT-160',
    KIT.SYSTEM_MQ_CHILD: 'KIT-125',
    KIT.SYSTEM_NYU_2008: 'KIT-157',
    KIT.SYSTEM_NYU_2009: 'KIT-157',
    KIT.SYSTEM_NYU_2010: 'KIT-157',
    KIT.SYSTEM_NYUAD_2011: 'KIT-AD',
    KIT.SYSTEM_NYUAD_2012: 'KIT-AD',
    KIT.SYSTEM_NYUAD_2014: 'KIT-AD',
    KIT.SYSTEM_UMD_2004: None,
    KIT.SYSTEM_UMD_2014_07: None,
    KIT.SYSTEM_UMD_2014_12: 'KIT-UMD-3',
}
# Names displayed in the info dict description
KIT_SYSNAMES = {
    KIT.SYSTEM_MQ_ADULT: 'Macquarie Dept of Cognitive Science (Adult), 2006-',
    KIT.SYSTEM_MQ_CHILD: 'Macquarie Dept of Cognitive Science (Child), 2006-',
    KIT.SYSTEM_AS: 'Academia Sinica, -2008',
    KIT.SYSTEM_AS_2008: 'Academia Sinica, 2008-',
    KIT.SYSTEM_NYU_2008: 'NYU New York, 2008-9',
    KIT.SYSTEM_NYU_2009: 'NYU New York, 2009-10',
    KIT.SYSTEM_NYU_2010: 'NYU New York, 2010-',
    KIT.SYSTEM_NYUAD_2011: 'New York University Abu Dhabi, 2011-12',
    KIT.SYSTEM_NYUAD_2012: 'New York University Abu Dhabi, 2012-14',
    KIT.SYSTEM_NYUAD_2014: 'New York University Abu Dhabi, 2014-',
    KIT.SYSTEM_UMD_2004: 'University of Maryland, 2004-14',
    KIT.SYSTEM_UMD_2014_07: 'University of Maryland, 2014',
    KIT.SYSTEM_UMD_2014_12: 'University of Maryland, 2014-',
}

LEGACY_AMP_PARAMS = {
    KIT.SYSTEM_NYU_2008: (5., 11.),
    KIT.SYSTEM_NYU_2009: (5., 11.),
    KIT.SYSTEM_NYU_2010: (5., 11.),
    KIT.SYSTEM_UMD_2004: (5., 11.),
}
