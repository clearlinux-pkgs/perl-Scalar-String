#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Scalar-String
Version  : 0.003
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Scalar-String-0.003.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Scalar-String-0.003.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libscalar-string-perl/libscalar-string-perl_0.003-1.debian.tar.xz
Summary  : 'string aspects of scalars'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Scalar-String-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Scalar::String - string aspects of scalars
DESCRIPTION
This module is about the string part of plain Perl scalars.  A scalar has
a string value, which is notionally a sequence of Unicode codepoints, but
may be internally encoded in either ISO-8859-1 or UTF-8.  In places, and
more so in older versions of Perl, the internal encoding shows through.
To fully understand Perl strings it is necessary to understand these
implementation details.

%package dev
Summary: dev components for the perl-Scalar-String package.
Group: Development
Provides: perl-Scalar-String-devel = %{version}-%{release}
Requires: perl-Scalar-String = %{version}-%{release}

%description dev
dev components for the perl-Scalar-String package.


%package perl
Summary: perl components for the perl-Scalar-String package.
Group: Default
Requires: perl-Scalar-String = %{version}-%{release}

%description perl
perl components for the perl-Scalar-String package.


%prep
%setup -q -n Scalar-String-0.003
cd %{_builddir}
tar xf %{_sourcedir}/libscalar-string-perl_0.003-1.debian.tar.xz
cd %{_builddir}/Scalar-String-0.003
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Scalar-String-0.003/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Scalar::String.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Scalar/String.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Scalar/String/String.so
