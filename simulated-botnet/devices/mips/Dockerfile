FROM busybox:uclibc
COPY qemu-mips-static /usr/bin/
COPY startup.sh /startup.sh
COPY www/ /www
RUN chmod +x /startup.sh
CMD ["/startup.sh"]
