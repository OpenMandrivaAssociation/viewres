Name: viewres
Version: 1.0.4
Release: 9
Summary:  graphical class browser for Xt
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xaw7)
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
