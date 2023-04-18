#!/bin/env python3

import os.path
import shutil

associations = [
  (
  # 'Capacitor_SMD.pretty/C_0805_2012Metric_Pad1.15x1.40mm_HandSolder.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/C_0805_2012Metric_Pad1.15x1.40mm_HandSolder.kicad_mod',
  ),(
  # 'Capacitor_SMD.pretty/C_1206_3216Metric_Pad1.42x1.75mm_HandSolder.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/C_1206_3216Metric_Pad1.42x1.75mm_HandSolder.kicad_mod',
  ),(
  # 'Package_DFN_QFN.pretty/DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm.kicad_mod',
  ),(
  # 'LIB_BE_PHELMA_CMS.pretty/Jack_3.5mm_PJ320D_Horizontal.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/Jack_3.5mm_PJ320D_Horizontal.kicad_mod',
  ),(
  # 'LED_SMD.pretty/LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder.kicad_mod',
  ),(
  # 'LED_SMD.pretty/LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder.kicad_mod',
  ),(
  # 'Potentiometer_SMD.pretty/Potentiometer_Vishay_TS53YL_Vertical.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/Potentiometer_Vishay_TS53YL_Vertical.kicad_mod',
  ),(
  # 'Resistor_SMD.pretty/R_0805_2012Metric_Pad1.15x1.40mm_HandSolder.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/R_0805_2012Metric_Pad1.15x1.40mm_HandSolder.kicad_mod',
  ),(
  # 'Resistor_SMD.pretty/R_1206_3216Metric_Pad1.42x1.75mm_HandSolder.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/R_1206_3216Metric_Pad1.42x1.75mm_HandSolder.kicad_mod',
  ),(
  # 'Package_SO.pretty/SOIC-8_3.9x4.9mm_P1.27mm.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/SOIC-8_3.9x4.9mm_P1.27mm.kicad_mod',
  ),(
  # 'Jumper.pretty/SolderJumper-2_P1.3mm_Open_TrianglePad1.0x1.5mm.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/SolderJumper-2_P1.3mm_Open_TrianglePad1.0x1.5mm.kicad_mod',
  ),(
  # 'TestPoint.pretty/TestPoint_Pad_D1.0mm.kicad_mod',
  # 'LIB_BE_PHELMA_CMS.pretty/TestPoint_Pad_D1.0mm.kicad_mod',
  ),

  (
  # 'LIB_BE_PHELMA.pretty/Banana_Mini_Jack_2Pin.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/Banana_Mini_Jack_2Pin.kicad_mod',
  ),(
  # 'Capacitor_THT.pretty/C_Disc_D8.0mm_W5.0mm_P5.00mm.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/CONDENSATEUR_5.08MM.kicad_mod',
  ),(
  # 'Capacitor_THT.pretty/C_Radial_D10.0mm_H12.5mm_P5.00mm.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/CONDENSATEUR_POL_5.08MM.kicad_mod',
  ),(
  # 'Diode_THT.pretty/D_A-405_P10.16mm_Horizontal.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/DIODE_10.16mm.kicad_mod',
  ),(
  # 'Package_DIP.pretty/DIP-8_W7.62mm_Socket_LongPads.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/DIP-8_W7.62mm_Socket_LongPads.kicad_mod',
  ),(
  # 'LIB_BE_PHELMA.pretty/Jack_3.5mm_CUI_SJ1-3533NG_Horizontal.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/Jack_3.5mm_CUI_SJ1-3533NG_Horizontal.kicad_mod',
  ),(
  'LED_THT.pretty/LED_D3.0mm.kicad_mod',
  'LIB_BE_PHELMA.pretty/LED_D3.0mm.kicad_mod',
  ),(
  # 'LED_THT.pretty/LED_D5.0mm.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/LED_D5.0mm.kicad_mod',
  ),(
  'OptoDevice.pretty/Osram_BPW82.kicad_mod',
  'LIB_BE_PHELMA.pretty/Osram_BPW82.kicad_mod',
  ),(
  # 'Connector_PinHeader_2.54mm.pretty/PinHeader_1x02_P2.54mm_Vertical.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/PinHeader_1x02_P2.54mm_Vertical.kicad_mod',
  ),(
  # 'Connector_PinHeader_2.54mm.pretty/PinHeader_1x03_P2.54mm_Vertical.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/PinHeader_1x03_P2.54mm_Vertical.kicad_mod',
  ),(
  # 'Potentiometer_THT.pretty/Potentiometer_Piher_PT-10-V10_Vertical.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/Potentiometer_Piher_PT-10-V10_Vertical.kicad_mod',
  ),(
  # 'Resistor_THT.pretty/R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal.kicad_mod',
  # 'LIB_BE_PHELMA.pretty/R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal.kicad_mod',
  ),
]


for asso in associations:
  if len(asso) == 2:
    src = '/usr/share/kicad/modules/' + asso[0]
    dst = asso[1]
    if os.path.exists(src):
      print(src,  dst)
      # shutil.copy(src, dst)
    else:
      print('Source', src, 'does not exist!')
