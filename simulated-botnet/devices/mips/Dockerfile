FROM busybox:uclibc
COPY qemu-mips-static /usr/bin/
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh
CMD ["/startup.sh"]
