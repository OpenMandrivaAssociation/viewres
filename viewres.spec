Name: viewres
Version: 1.0.4
Release: 1
Summary:  graphical class browser for Xt
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The viewres program displays a tree showing the widget class hierarchy of the
Athena Widget Set.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/viewres
%{_datadir}/X11/app-defaults/Viewres
%{_datadir}/X11/app-defaults/Viewres-color
%{_mandir}/man1/viewres.*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 670766
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 591905
- new release

* Thu Dec 17 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 479714
- New version: 1.0.2
  New binary: Viewres-color

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-10mdv2010.0
+ Revision: 427493
- rebuild

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.1-9mdv2009.1
+ Revision: 366569
- no more autoreconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2009.0
+ Revision: 225917
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-7mdv2008.1
+ Revision: 166442
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-6mdv2008.1
+ Revision: 156426
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2008.0
+ Revision: 67298
- fix man pages extension


* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 20:47:59 (59448)
- rebuild to fix libXaw.so.8 dependency

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:26:44 (31744)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:19:51 (27491)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

