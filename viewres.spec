Name: viewres
Version: 1.0.1
Release: %mkrel 7
Summary:  graphical class browser for Xt
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The viewres program displays a tree showing the widget class hierarchy of the
Athena Widget Set.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -ifs
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/viewres
%{_datadir}/X11/app-defaults/Viewres
%{_mandir}/man1/viewres.*
