"""Register built-in games (idempotent)."""

_registered = False


def ensure_builtins_registered() -> None:
    """Register all built-in games. Safe to call multiple times."""
    global _registered
    if _registered:
        return
    from arena.games import register_game
    from arena.games.ultimatum import UltimatumGame
    from arena.games.first_price_auction import FirstPriceAuctionGame
    from arena.games.principal_agent import PrincipalAgentGame
    from arena.games.bilateral_trade import BilateralTradeGame
    from arena.games.provision_point import ProvisionPointGame
    from arena.games.all_pay_auction import AllPayAuctionGame
    from arena.games.hold_up import HoldUpGame
    from arena.games.war_of_attrition import WarOfAttritionGame
    from arena.games.dutch_auction import DutchAuctionGame

    register_game(UltimatumGame())
    register_game(FirstPriceAuctionGame())
    register_game(PrincipalAgentGame())
    register_game(BilateralTradeGame())
    register_game(ProvisionPointGame())
    register_game(AllPayAuctionGame())
    register_game(HoldUpGame())
    register_game(WarOfAttritionGame())
    register_game(DutchAuctionGame())

    _registered = True
