from playwright.sync_api import Locator


class SideMenu:
    """
    Dumb component: returns locators only.
    All assertions/checks are done in tests.
    """

    def __init__(self, root: Locator):
        self.root = root

    # ---------------------------
    # Base collections
    # ---------------------------
    @property
    def top_items(self) -> Locator:
        """All top-level <li> items."""
        return self.root.locator(":scope > ul > li")

    @property
    def all_links(self) -> Locator:
        """All <a> links inside side menu (any level)."""
        return self.root.locator("a.l1dqjhvv")

    # ---------------------------
    # Helpers (still locators only)
    # ---------------------------
    def group_item(self, title: str) -> Locator:
        """
        Returns top-level LI that contains group title (e.g. 'Cloud Servers', 'Networks', etc.)
        """
        return (
            self.root
            .locator(":scope > ul > li")
            .filter(has=self.root.get_by_text(title, exact=True))
            .first
        )

    def group_links(self, group_title: str) -> Locator:
        """Returns <a> links inside a group submenu."""
        return self.group_item(group_title).locator("ul > li a.l1dqjhvv")

    def link_by_text(self, text: str) -> Locator:
        """Any link in the menu by visible text."""
        return self.root.get_by_role("link", name=text, exact=True)

    # ---------------------------
    # Top-level items (explicit properties)
    # ---------------------------
    @property
    def enterprise_bare_metal_group(self) -> Locator:
        return self.root.locator("ul > li", has_text="Enterprise Bare Metal").first

    @property
    def cloud_servers_group(self) -> Locator:
        return self.group_item("Cloud Servers")

    @property
    def networks_group(self) -> Locator:
        return self.group_item("Networks")

    @property
    def identity_and_access_group(self) -> Locator:
        return self.group_item("Identity and Access")

    @property
    def billing_group(self) -> Locator:
        return self.group_item("Billing")

    @property
    def reports_group(self) -> Locator:
        return self.group_item("Reports")

    # ---------------------------
    # Single-link top-level items
    # ---------------------------
    @property
    def cloud_storage_link(self) -> Locator:
        return self.link_by_text("Cloud Storage")

    @property
    def managed_kubernetes_link(self) -> Locator:
        return self.link_by_text("Managed Kubernetes")

    @property
    def load_balancers_link(self) -> Locator:
        return self.link_by_text("Load Balancers")

    @property
    def firewalls_link(self) -> Locator:
        return self.link_by_text("Firewalls")

    @property
    def private_racks_link(self) -> Locator:
        return self.link_by_text("Private Racks")

    @property
    def monitoring_text_item(self) -> Locator:
        return self.root.get_by_text("Monitoring", exact=True)

    @property
    def ssl_certificates_link(self) -> Locator:
        return self.link_by_text("SSL certificates")

    @property
    def account_settings_link(self) -> Locator:
        return self.link_by_text("Account settings")

    @property
    def requests_link(self) -> Locator:
        return self.link_by_text("Requests")

    # ---------------------------
    # Submenu links (explicit properties)
    # ---------------------------
    # Enterprise Bare Metal
    @property
    def ebm_manage_link(self) -> Locator:
        return self.enterprise_bare_metal_group.get_by_role(
            "link", name="Manage", exact=True
        )

    @property
    def ebm_order_link(self) -> Locator:
        return self.enterprise_bare_metal_group.get_by_role(
            "link", name="Order", exact=True
        )

    # Cloud Servers
    @property
    def cloud_create_manage_link(self) -> Locator:
        return self.cloud_servers_group.get_by_role(
            "link", name="Create & Manage", exact=True
        )

    @property
    def cloud_snapshots_backups_link(self) -> Locator:
        return self.cloud_servers_group.get_by_role(
            "link", name="Snapshots & Backups", exact=True
        )

    @property
    def cloud_images_link(self) -> Locator:
        return self.cloud_servers_group.get_by_role("link", name="Images", exact=True)

    @property
    def cloud_volumes_link(self) -> Locator:
        return self.cloud_servers_group.get_by_role("link", name="Volumes", exact=True)

    # Networks
    @property
    def networks_direct_connect_link(self) -> Locator:
        return self.networks_group.get_by_role(
            "link", name="Direct Connect", exact=True
        )

    @property
    def networks_l2_segments_link(self) -> Locator:
        return self.networks_group.get_by_role("link", name="L2 Segments", exact=True)

    @property
    def networks_dns_link(self) -> Locator:
        return self.networks_group.get_by_role("link", name="DNS", exact=True)

    @property
    def networks_vpn_access_link(self) -> Locator:
        return self.networks_group.get_by_role("link", name="VPN access", exact=True)

    # Identity and Access
    @property
    def iam_ssh_gpg_keys_link(self) -> Locator:
        return self.identity_and_access_group.get_by_role(
            "link", name="SSH & GPG keys", exact=True
        )

    @property
    def iam_api_tokens_link(self) -> Locator:
        return self.identity_and_access_group.get_by_role(
            "link", name="API tokens", exact=True
        )

    # Billing
    @property
    def billing_orders_link(self) -> Locator:
        return self.billing_group.get_by_role("link", name="Orders", exact=True)

    @property
    def billing_invoices_link(self) -> Locator:
        return self.billing_group.get_by_role("link", name="Invoices", exact=True)

    @property
    def billing_group_invoices_link(self) -> Locator:
        return self.billing_group.get_by_role("link", name="Group invoices", exact=True)

    @property
    def billing_account_statement_link(self) -> Locator:
        return self.billing_group.get_by_role(
            "link", name="Account statement", exact=True
        )

    @property
    def billing_payment_details_link(self) -> Locator:
        return self.billing_group.get_by_role(
            "link", name="Payment details", exact=True
        )

    @property
    def billing_top_up_balance_link(self) -> Locator:
        return self.billing_group.get_by_role("link", name="Top up balance", exact=True)

    # Reports
    @property
    def reports_cloud_servers_link(self) -> Locator:
        return self.reports_group.get_by_role("link", name="Cloud Servers", exact=True)

    @property
    def reports_cloud_storage_link(self) -> Locator:
        return self.reports_group.get_by_role("link", name="Cloud Storage", exact=True)
