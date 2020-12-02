#!/usr/bin/perl
use strict;
use Data::Dumper;

my $valid = 0;

foreach my $line (<STDIN>) {
        chomp($line);
        my @parts = ($line =~ /^(\d+)\-(\d+) ([a-z]): (\S+)$/g);
        my $this_valid = 0;
        my $a=(substr($parts[3], $parts[0]-1, 1) eq $parts[2]);
        my $b=(substr($parts[3], $parts[1]-1, 1) eq $parts[2]);
        if (($a+$b)== 1) { $valid++; }
}

print "$valid\n";
