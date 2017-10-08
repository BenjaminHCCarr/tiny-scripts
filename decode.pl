#!/usr/bin/perl

#Scriptname: decode.pl

use strict;

use MIME::Base64;

use URI::Escape;

local($/) = undef; # slurp

my $decoded = decode_base64();

$decoded =~ s/&/\n/gms;

$decoded =~ s/%20/\ /gms;

$decoded =~ s/%3a/\:/gms;

my $decoded2 = uri_unescape($decoded);

print $decoded2;

### End of Perl Script ###
