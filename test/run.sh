echo -e 'running noizu.py clang_log -e CMSIS STM32F4xx_HAL_Driver'
python ../noizu.py clang_log -e CMSIS STM32F4xx_HAL_Driver

echo -e '\n\n'

echo -e 'running noizu.py gcc_log -e CMSIS STM32F4xx_HAL_Driver'
python ../noizu.py gcc_log -e CMSIS STM32F4xx_HAL_Driver
