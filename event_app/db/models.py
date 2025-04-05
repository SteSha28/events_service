from sqlalchemy import BigInteger, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from event_app.db.database import Base

import datetime


class Location(Base):
    __tablename__ = 'location'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        )
    name: Mapped[str] = mapped_column(
        nullable=False,
        )
    address: Mapped[str]
    geolocation: Mapped[str] = mapped_column(
        nullable=False,
        )
    description: Mapped[str]

    events: Mapped[list["Event"]] = relationship(
        back_populates="location",
        cascade="all,delete-orphan",
        passive_deletes=True,
        )


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True,
        )
    name: Mapped[str] = mapped_column(
        nullable=False,
        )

    events: Mapped[list["Event"]] = relationship(
        back_populates='category',
        passive_deletes=True,
        )


event_has_tag = Table(
    "event_tag",
    Base.metadata,
    Column(
        "event_id",
        BigInteger,
        ForeignKey("event.id", ondelete="CASCADE"),
        primary_key=True,
        ),
    Column(
        "tag_id",
        BigInteger,
        ForeignKey("tag.id", ondelete="CASCADE"),
        primary_key=True
        ),
)


class Tag(Base):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
    )

    events: Mapped[list["Event"]] = relationship(
        "Event",
        secondary=event_has_tag,
        back_populates="tags"
    )


class Event(Base):
    __tablename__ = 'event'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True,
        )
    title: Mapped[str] = mapped_column(
        nullable=False,
        )
    description: Mapped[str]
    date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        )
    price: Mapped[str] = mapped_column(
        nullable=False
    )
    url: Mapped[str] = mapped_column(
        nullable=False,
        )
    location_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("location.id",
                   ondelete="CASCADE",
                   ),
        nullable=False,
        )
    category_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("category.id",
                   ondelete="SET NULL",
                   ),
        nullable=True,
        )

    location: Mapped["Location"] = relationship(
        back_populates="events",
        )
    category: Mapped["Category"] = relationship(
        back_populates="events",
        )
    tags: Mapped[list["Tag"]] = relationship(
        "Tag",
        secondary=event_has_tag,
        back_populates="events",
    )
