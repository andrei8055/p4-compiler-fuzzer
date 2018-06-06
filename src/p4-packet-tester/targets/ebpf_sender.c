/*
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 */

#include <arpa/inet.h>
#include <linux/if_packet.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <net/if.h>
#include <netinet/ether.h>
#include <netinet/ip.h>
#include <netinet/in.h>
#include <netinet/ip_icmp.h>
#include <errno.h>


#define MY_DEST_MAC0	0x00
#define MY_DEST_MAC1	0x00
#define MY_DEST_MAC2	0x00
#define MY_DEST_MAC3	0x00
#define MY_DEST_MAC4	0x00
#define MY_DEST_MAC5	0x00

#define DEFAULT_IF	"enp0s3"
#define BUF_SIZ		1024
#define DEFAULT_PACKET "000000"

char map_bin_to_hex(char *c)
   {
      if(!strcmp(c, "0000"))      return '0';
      else if(!strcmp(c, "0001")) return '1';
      else if(!strcmp(c, "0010")) return '2';
      else if(!strcmp(c, "0011")) return '3';
      else if(!strcmp(c, "0100")) return '4';
      else if(!strcmp(c, "0101")) return '5';
      else if(!strcmp(c, "0110")) return '6';
      else if(!strcmp(c, "0111")) return '7';
      else if(!strcmp(c, "1000")) return '8';
      else if(!strcmp(c, "1001")) return '9';
      else if(!strcmp(c, "1010")) return 'A';
      else if(!strcmp(c, "1011")) return 'B';
      else if(!strcmp(c, "1100")) return 'C';
      else if(!strcmp(c, "1101")) return 'D';
      else if(!strcmp(c, "1110")) return 'E';
      else if(!strcmp(c, "1111")) return 'F';
   }

int conv(char c)
   {
      if((c == '0'))      return 0;
      else if(c == '1') return 1;
      else if(c == '2') return 2;
      else if(c == '3') return 3;
      else if(c == '4') return 4;
      else if(c == '5') return 5;
      else if(c == '6') return 6;
      else if(c == '7') return 7;
      else if(c == '8') return 8;
      else if(c == '9') return 9;
      else if(c == 'A') return 10;
      else if(c == 'B') return 11;
      else if(c == 'C') return 12;
      else if(c == 'D') return 13;
      else if(c == 'E') return 14;
      else if(c == 'F') return 15;
      return 0;
   }

 void bin_array_to_hex(char *b, int length, char* result)
 {
    int i, j, k;
      for(i = 0; i < length; i+=4)
      {
	char hexB[5];
         for(k = 0, j = i; j < (i+4); j++, k++)
         {
            hexB[k] = b[j];
 	 }
	 hexB[4]='\0';
         char hex_c = map_bin_to_hex(hexB);
	 int bin_c = conv(hex_c);
	 if((i/4) % 2 == 0){
		result[i/8] = (result[i/8] & ~(15<<4)) | bin_c<<4;
		char val = result[i/8] & 15<<4;
	 } else {
	 	result[i/8] = (result[i/8] & ~15) | bin_c;
		char val = result[i/8] & 15;
	 }
      }
  }


int main(int argc, char *argv[])
{
	int sockfd;

	struct ifreq if_idx;
	struct ifreq if_mac;
	int tx_len = 0;
	char sendbuf[BUF_SIZ];
	struct sockaddr_ll socket_address;
	char ifName[IFNAMSIZ];
	char packet[BUF_SIZ];

	/* Get interface name */
	if (argc > 1)
		strcpy(ifName, argv[1]);
	else
		strcpy(ifName, DEFAULT_IF);

	if (argc > 2)
                strcpy(packet, argv[2]);
        else
                strcpy(packet, DEFAULT_PACKET);

	int max_packet_size = sizeof(packet)/sizeof(packet[0]);
	int packet_size = 0;
	for(int i = 0; i < max_packet_size; i++){
		if(packet[i] == 0){
			break;
		}
		packet_size++;
	}
	tx_len = packet_size / 8;

	char result[1024];
	bin_array_to_hex(packet, packet_size, result);

	/* Open RAW socket to send on */
	if ((sockfd = socket(AF_PACKET, SOCK_RAW, IPPROTO_RAW)) == -1) {
	    perror("socket");
	}

	/* Get the index of the interface to send on */
	memset(&if_idx, 0, sizeof(struct ifreq));
	strncpy(if_idx.ifr_name, ifName, IFNAMSIZ-1);
	if (ioctl(sockfd, SIOCGIFINDEX, &if_idx) < 0)
	    perror("SIOCGIFINDEX");
	/* Get the MAC address of the interface to send on */
	memset(&if_mac, 0, sizeof(struct ifreq));
	strncpy(if_mac.ifr_name, ifName, IFNAMSIZ-1);
	if (ioctl(sockfd, SIOCGIFHWADDR, &if_mac) < 0)
	    perror("SIOCGIFHWADDR");

	/* Construct the Ethernet header */
	memset(sendbuf, 0, BUF_SIZ);

	/* Index of the network device */
	socket_address.sll_ifindex = if_idx.ifr_ifindex;
	/* Address length*/
	socket_address.sll_halen = ETH_ALEN;
	/* Destination MAC */
	socket_address.sll_addr[0] = MY_DEST_MAC0;
	socket_address.sll_addr[1] = MY_DEST_MAC1;
	socket_address.sll_addr[2] = MY_DEST_MAC2;
	socket_address.sll_addr[3] = MY_DEST_MAC3;
	socket_address.sll_addr[4] = MY_DEST_MAC4;
	socket_address.sll_addr[5] = MY_DEST_MAC5;

	/* Send packet */
	int ret = sendto(sockfd, result, tx_len, 0, (struct sockaddr*)&socket_address, sizeof(struct sockaddr_ll));
	if(ret == -1)
	    printf("Send failed %s", strerror(errno));
	else
	    printf("Send okay :)");

	return 0;
}