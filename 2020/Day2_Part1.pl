#!/usr/bin/perl
use strict;
use Data::Dumper;

my $valid = 0;

foreach my $line (<STDIN>) {
        chomp($line);
        my @parts = ($line =~ /^(\d+)\-(\d+) ([a-z]): (\S+)$/g);
        my $count = () = ($parts[3] =~ /$parts[2]/g);
        print "$parts[0] $parts[1] $parts[2] $parts[3] $count\n";
        if ($count >= $parts[0] && $count <= $parts[1]) { $valid++; }
}
