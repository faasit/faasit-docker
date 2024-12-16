cd /mitosis/mitosis-core/exp/criu-micro
bash host_dump.sh > /dev/null 2>&1

sleep 1

bash run_benchmark.sh 100 my_container /mitosis/mitosis-core/exp/criu-micro 2>/dev/null