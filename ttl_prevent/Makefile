obj-m += prevent_ttl.o
# Include the json-c header file.
all:
	
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

ins:
	sudo dmesg -C
	sudo insmod prevent_ttl.ko

rm:
	sudo rmmod prevent_ttl


