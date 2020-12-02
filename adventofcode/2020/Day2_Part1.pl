#!/usr/bin/perl
use strict;
use Data::Dumper;

my $valid = 0;

foreach my $line (<STDIN>) {
        chomp($line);
        my @parts = ($line =~ /^(\d+)\-(\d+) ([a-z]): (\S+)$/g);
        my $count = () = ($parts[3] =~ /$parts[2]/g);
        if ($count >= $parts[0] && $count <= $parts[1]) { $valid++; }
}
